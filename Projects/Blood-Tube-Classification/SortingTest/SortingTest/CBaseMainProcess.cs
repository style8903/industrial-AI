using System;
using System.Threading;

namespace SortingTest
{
    internal class CBaseMainProcess
    {
        Thread main_thread;
        private int start_step;
        CBaseSlave slave = new CBaseSlave();
        public static bool tube_in;
        public int delay_tick;
        private bool start_flag;
        DateTime dateTime = new DateTime();

        internal void Start()
        {
            main_thread = new Thread(new ThreadStart(Main_Process));
            main_thread.Start();
            start_flag = true;
        }

        private void Main_Process()
        {
            while(start_flag)
            {
                switch (start_step)
                {
                    case 0:
                        start_step++;
                        break;
                    case 1:
                        slave.Start();
                        start_step++;
                        break;
                    case 2:
                        if (tube_in)
                        {
                            tube_in = false;
                            Fm_Main.fm_Main.ClearText();
                            start_step++;
                        }
                        break;
                    case 3:
                        dateTime = DateTime.Now;
                        start_step++;
                        break;
                    case 4:
                        if (Time_Check(dateTime, delay_tick))
                            start_step++;
                        break;
                    case 5:
                        Fm_Main.fm_Main.CaptureImage();
                        start_step++;
                        break;
                    case 6:
                        start_step = 2;
                        break;
                }
            }
        }

        internal void Stop()
        {
            start_step = 0;
            start_flag = false;

            slave.Stop();

            if (main_thread != null && main_thread.IsAlive)
            {
                main_thread.Abort();
            }
        }

        /// <summary>
        /// 시간 딜레이 함수
        /// </summary>
        /// <param name="Start_time">시작 시간</param>
        /// <param name="MS">딜레이 시간(ms)</param>
        /// <returns>딜레이 시간 경과시 true 반환</returns>
        private static bool Time_Check(DateTime Start_time, int MS)
        {

            DateTime Now_time = DateTime.Now;
            TimeSpan delay_tick = new TimeSpan(0, 0, 0, 0, MS);
            DateTime Add_time = Start_time.Add(delay_tick);

            if (Now_time >= Add_time)
            {
                return true;
            }
            else
                return false;
        }

        
    }
}