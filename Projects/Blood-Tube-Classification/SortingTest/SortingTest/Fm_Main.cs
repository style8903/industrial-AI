using Microsoft.WindowsAPICodePack.Dialogs;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using OpenCvSharp;
using OpenCvSharp.Extensions;

namespace SortingTest
{
    public partial class Fm_Main : Form
    {
        
        public static Fm_Main fm_Main;
        static int cnt;
        private String bdPort = string.Empty;
        private String filPath = string.Empty;
        CBaseMainProcess mainProcess = new CBaseMainProcess();
        CBaseML ml = new CBaseML();
        private static VideoCapture capture;

        public Fm_Main()
        {
            InitializeComponent();
            fm_Main = this;

            capture = new VideoCapture();
            capture.Set(VideoCaptureProperties.FrameHeight, 480);
            capture.Set(VideoCaptureProperties.FrameWidth, 640);
            capture.Set(VideoCaptureProperties.Fps, 60);
            //capture.Set(VideoCaptureProperties.Exposure, 80);
        }

        internal void ClearText()
        {
            this.Invoke(new Action(delegate ()
            {
                lb_Result.Text = "null";
                pBox_CaptureImg.Image = null;
            }));
        }

        private void Fm_Main_Load(object sender, EventArgs e)
        {
            foreach (string port in SerialPort.GetPortNames())
            {
                cbo_Portnum.Items.Add(port);
            }

            capture.Open(2, VideoCaptureAPIs.ANY);
            if (!capture.IsOpened())
            {
                Close();
                return;
            }
            backgroundWorker1.RunWorkerAsync();

            //저장값 불러오기
            Load_User_Properties();
            ml.CreateModel();
            cnt = 0;
        }

        private void Load_User_Properties()
        {
            //기존 Port 번호 불러오기
            bdPort = Properties.Settings.Default.BDPort;

            //기존 저장경로 불러오기
            filPath = Properties.Settings.Default.filePath;
        }

        private void btn_Start_Click(object sender, EventArgs e)
        {
            mainProcess.Start();
        }

        private void btn_Stop_Click(object sender, EventArgs e)
        {
            mainProcess.Stop();
        }

        public void CaptureImage()
        {
            this.Invoke(new Action(delegate ()
            {
                Bitmap bitmap = (Bitmap)pbox_Realtime.Image.Clone();
                string result = ml.PredictResult(bitmap);
                lb_Result.Text = result;
                pBox_CaptureImg.Image = bitmap;
                //string save_name = DateTime.Now.ToString("yyyy-MM-dd-hh시mm분ss초");
                string save_name = $"{cnt}_{result}";
                cnt++;
                string save_folder = string.Format(@"{0}\{1}.jpg", filPath, save_name);
                pBox_CaptureImg.Image.Save(save_folder, System.Drawing.Imaging.ImageFormat.Jpeg);
            }));
        }
        

        private void btn__PortSet_Click(object sender, EventArgs e)
        {
            bdPort = cbo_Portnum.SelectedIndex.ToString();
            Properties.Settings.Default.BDPort = bdPort;
            Properties.Settings.Default.Save();
        }

        private void btn_TimeSet_Click(object sender, EventArgs e)
        {
            mainProcess.delay_tick = (int)nud_TimeData.Value;
        }

        private void btn_FilePath_Click(object sender, EventArgs e)
        {
            //Dialog 객체 생성 및 파일 경로 선택
            CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.IsFolderPicker = true;
            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                filPath = dialog.FileName;
                Properties.Settings.Default.filePath = filPath;
                Properties.Settings.Default.Save();
                Console.WriteLine("저장 경로 : " + filPath);
            }
            else
            {
                return;
            }
        }

        private void Fm_Main_FormClosing(object sender, FormClosingEventArgs e)
        {
            backgroundWorker1.CancelAsync();
            capture.Dispose();
        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            var bgWorker = (BackgroundWorker)sender;

            while (!bgWorker.CancellationPending)
            {
                using (var frameMat = capture.RetrieveMat())
                {
                    var frameBitmap = BitmapConverter.ToBitmap(frameMat);
                    bgWorker.ReportProgress(0, frameBitmap);
                }
                Thread.Sleep(1);
            }
        }

        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            var frameBitmap = (Bitmap)e.UserState;
            pbox_Realtime.Image?.Dispose();
            pbox_Realtime.Image = frameBitmap;
        }

        private void btn_Capture_Click(object sender, EventArgs e)
        {
            CaptureImage();
        }

        private void btn_test_Click(object sender, EventArgs e)
        {
            ml.CreateModel();
        }
    }
}
