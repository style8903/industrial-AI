using System;
using System.Diagnostics;

namespace SortingTest
{
    internal class CBaseSlave
    {
        public bool tube_in;
        internal string port_name;
        CBaseSerialComm comm = new CBaseSerialComm();

        public CBaseSlave()
        {
            comm.OpenComm("COM21", 9600);
        }
        public CBaseSlave(bool on)
        {
            this.tube_in = on;
        }

        internal bool Init()
        {
            throw new NotImplementedException();
        }

        internal void Start()
        {
            byte[] buf = new byte[8];
            byte[] tmp = new byte[2];
            ushort crc;

            tmp[0] = 1 & 0xff;
            tmp[1] = 5 & 0xff;
            crc = comm.CalcCRC16(tmp, 2);
            
            buf[0] = CBaseSerialComm.DLE;
            buf[1] = CBaseSerialComm.STX;
            buf[2] = 1 & 0xff;
            buf[3] = 5 & 0xff;
            buf[4] = (byte)(crc & 0xff);
            buf[5] = (byte)(crc >>= 8);
            buf[6] = CBaseSerialComm.DLE;
            buf[7] = CBaseSerialComm.ETX;

            comm.Send(buf);

            Debug.WriteLine(buf);
        }

        internal void Stop()
        {
            byte[] buf = new byte[8];
            byte[] tmp = new byte[2];
            ushort crc;

            tmp[0] = 1 & 0xff;
            tmp[1] = 6 & 0xff;
            crc = comm.CalcCRC16(tmp, 2);

            buf[0] = CBaseSerialComm.DLE;
            buf[1] = CBaseSerialComm.STX;
            buf[2] = 1 & 0xff;
            buf[3] = 6 & 0xff;
            buf[4] = (byte)(crc & 0xff);
            buf[5] = (byte)(crc >>= 8);
            buf[6] = CBaseSerialComm.DLE;
            buf[7] = CBaseSerialComm.ETX;

            Debug.WriteLine(buf);

            comm.Send(buf);
        }
    }
}