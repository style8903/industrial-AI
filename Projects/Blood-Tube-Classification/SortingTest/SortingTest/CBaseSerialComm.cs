using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace SortingTest
{
    class CBaseSerialComm
    {
        public delegate void DataReceivedHandlerFunc(byte[] receiveData);
        public DataReceivedHandlerFunc DataReceivedHandler;
        public delegate void DisconnectedHandlerFunc();
        public DisconnectedHandlerFunc DisconnectedHandler;
        private byte[] dataBuf = new byte[100];
        public Queue<byte> bytesBufferQueue = new Queue<byte>();

        int buf_idx = 0;
        bool dle_flag = false;
        bool stx_flag = false;

        public const Byte STX = 0x02;
        public const Byte ETX = 0x03;
        public const Byte DLE = 0x10;

        private SerialPort serialPort;

        public bool IsOpen
        {
            get
            {
                if (serialPort != null) return serialPort.IsOpen;
                return false;
            }
        }

        // serial port check
        private Thread threadCheckSerialOpen;
        private bool isThreadCheckSerialOpen = false;


        public bool OpenComm(string portName, int baudrate)
        {
            try
            {
                serialPort = new SerialPort();

                serialPort.PortName = portName;
                serialPort.BaudRate = baudrate;
                serialPort.DataBits = 8;
                serialPort.StopBits = StopBits.One;
                serialPort.Parity = Parity.None;

                serialPort.ErrorReceived += serialPort_ErrorReceived;
                serialPort.DataReceived += serialPort_DataReceived;

                serialPort.Open();

                StartCheckSerialOpenThread();
                return true;
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
                return false;
            }
        }

        public void CloseComm()
        {
            try
            {
                if (serialPort != null)
                {
                    StopCheckSerialOpenThread();
                    serialPort.Close();
                    serialPort = null;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
        }

        public bool Send(string sendData)
        {
            try
            {
                if (serialPort != null && serialPort.IsOpen)
                {
                    serialPort.Write(sendData);
                    return true;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
            return false;
        }

        public bool Send(byte[] sendData)
        {
            try
            {
                if (serialPort != null && serialPort.IsOpen)
                {
                    serialPort.Write(sendData, 0, sendData.Length);
                    return true;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
            return false;
        }

        public bool Send(byte[] sendData, int offset, int count)
        {
            try
            {
                if (serialPort != null && serialPort.IsOpen)
                {
                    serialPort.Write(sendData, offset, count);
                    return true;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
            return false;
        }

        public bool Send(byte[] sendData, int count)
        {
            try
            {
                if (serialPort != null && serialPort.IsOpen)
                {
                    serialPort.Write(sendData, 0, count);
                    return true;
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
            return false;
        }

        private byte[] ReadSerialByteData()
        {
            /*serialPort.ReadTimeout = 100;*/
            byte[] bytesBuffer = new byte[serialPort.BytesToRead];
            int bufferOffset = 0;
            int bytesToRead = serialPort.BytesToRead;

            while (bytesToRead > 0)
            {
                try
                {
                    int readBytes = serialPort.Read(bytesBuffer, bufferOffset, bytesToRead - bufferOffset);
                    bytesToRead -= readBytes;
                    bufferOffset += readBytes;
                }
                catch (TimeoutException ex)
                {
                    Debug.WriteLine(ex.ToString());
                }
            }

            return bytesBuffer;
        }

        private void serialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            try
            {
                byte[] bytesBuffer = ReadSerialByteData();
                int cnt = bytesBuffer.Length;
                
                if(cnt > 0)
                {
                    Debug.WriteLine(bytesBuffer);
                    RecvData(bytesBuffer, cnt);
                }

            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.ToString());
            }
        }

        private void RecvData(byte[] bytesBuffer, int cnt)
        {
            Byte ch;
            int i;

            for (i = 0; i <= cnt - 1; i++)
            {
                ch = bytesBuffer[i];

                if ((ch == DLE) && (dle_flag == false))
                {
                    dle_flag = true;
                    continue;
                }

                if (dle_flag)
                {
                    dle_flag = false;
                    if (ch == STX)
                    {
                        stx_flag = true;

                        buf_idx = 0;
                        continue;
                    }
                    else if (ch == ETX)
                    {
                        stx_flag = false;
                        buf_idx = 0;
                        continue;
                    }
                }

                if (stx_flag)
                {
                    dataBuf[buf_idx++] = ch;

                    ParsingData();

                    if (buf_idx == 0)
                        stx_flag = false;
                }
                else
                    buf_idx = 0;

            }
        }

        private void ParsingData()
        {
            int data_len;

            if (buf_idx > 2)
            {
                data_len = dataBuf[0];

                int crc_idx = data_len + 3;

                if(buf_idx == crc_idx)
                {
                    ushort recv_crc = (ushort)(((0xFFFF & dataBuf[buf_idx]) << 8) | (dataBuf[buf_idx - 1] & 0xFF));

                    if (CalcCRC16(dataBuf, buf_idx - 1) == recv_crc)
                    {
                        if(dataBuf[1] == 0x05)
                        {
                            CBaseMainProcess.tube_in = true;
                        }
                    }
                }
            }                
        }

        public ushort CalcCRC16(byte[] dataBuf, int calc_size)
        {
            ushort i, j, crc;
            crc = 0xFFFF;

            for (i = 0; i <= calc_size - 1; i++)
            {
                crc ^= dataBuf[i];
                for (j = 0; j <= 7; j++)
                {
                    if ((crc & 0x01) == 0x01)
                    {
                        //crc >>= 1;
                        //crc ^= 0xA001;
                        crc = (ushort)((crc >> 1) ^ 0xA001);
                    }
                    else
                    {
                        crc >>= 1;
                    }
                }
            }

            return (crc);
        }

        private void serialPort_ErrorReceived(object sender, SerialErrorReceivedEventArgs e)
        {
            Debug.WriteLine(e.ToString());
        }

        private void StartCheckSerialOpenThread()
        {
            isThreadCheckSerialOpen = true;
            threadCheckSerialOpen = new Thread(new ThreadStart(ThreadCheckSerialOpen));
            threadCheckSerialOpen.Start();
        }

        private void StopCheckSerialOpenThread()
        {
            if (isThreadCheckSerialOpen)
            {
                isThreadCheckSerialOpen = false;
                if (Thread.CurrentThread != threadCheckSerialOpen)
                    threadCheckSerialOpen.Join();
            }
        }

        private void ThreadCheckSerialOpen()
        {
            while (isThreadCheckSerialOpen)
            {
                Thread.Sleep(100);

                try
                {
                    if (serialPort == null || !serialPort.IsOpen)
                    {
                        Debug.WriteLine("seriaport disconnected");
                        if (DisconnectedHandler != null)
                            DisconnectedHandler();
                        break;
                    }
                }
                catch (Exception ex)
                {
                    Debug.WriteLine(ex.ToString());
                }
            }
        }
    }
}
