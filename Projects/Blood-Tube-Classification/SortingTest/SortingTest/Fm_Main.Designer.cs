
namespace SortingTest
{
    partial class Fm_Main
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.cbo_Portnum = new System.Windows.Forms.ComboBox();
            this.lb_PortName = new System.Windows.Forms.Label();
            this.btn__PortSet = new System.Windows.Forms.Button();
            this.lb_TimeName = new System.Windows.Forms.Label();
            this.nud_TimeData = new System.Windows.Forms.NumericUpDown();
            this.btn_TimeSet = new System.Windows.Forms.Button();
            this.btn_FilePath = new System.Windows.Forms.Button();
            this.pbox_Realtime = new System.Windows.Forms.PictureBox();
            this.lb_ResultTitle = new System.Windows.Forms.Label();
            this.lb_Result = new System.Windows.Forms.Label();
            this.btn_Start = new System.Windows.Forms.Button();
            this.btn_Stop = new System.Windows.Forms.Button();
            this.pBox_CaptureImg = new System.Windows.Forms.PictureBox();
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.btn_Capture = new System.Windows.Forms.Button();
            this.btn_test = new System.Windows.Forms.Button();
            this.pBox_type1 = new System.Windows.Forms.PictureBox();
            this.pBox_type2 = new System.Windows.Forms.PictureBox();
            this.pBox_type3 = new System.Windows.Forms.PictureBox();
            this.pBox_type4 = new System.Windows.Forms.PictureBox();
            this.pBox_type5 = new System.Windows.Forms.PictureBox();
            this.pBox_type6 = new System.Windows.Forms.PictureBox();
            this.pBox_type7 = new System.Windows.Forms.PictureBox();
            this.pBox_type8 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.nud_TimeData)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbox_Realtime)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_CaptureImg)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type6)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type7)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type8)).BeginInit();
            this.SuspendLayout();
            // 
            // cbo_Portnum
            // 
            this.cbo_Portnum.FormattingEnabled = true;
            this.cbo_Portnum.Location = new System.Drawing.Point(23, 46);
            this.cbo_Portnum.Name = "cbo_Portnum";
            this.cbo_Portnum.Size = new System.Drawing.Size(120, 20);
            this.cbo_Portnum.TabIndex = 0;
            // 
            // lb_PortName
            // 
            this.lb_PortName.AutoSize = true;
            this.lb_PortName.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_PortName.Location = new System.Drawing.Point(41, 14);
            this.lb_PortName.Name = "lb_PortName";
            this.lb_PortName.Size = new System.Drawing.Size(80, 21);
            this.lb_PortName.TabIndex = 1;
            this.lb_PortName.Text = "Com Port";
            // 
            // btn__PortSet
            // 
            this.btn__PortSet.Font = new System.Drawing.Font("Nirmala UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn__PortSet.Location = new System.Drawing.Point(159, 41);
            this.btn__PortSet.Name = "btn__PortSet";
            this.btn__PortSet.Size = new System.Drawing.Size(68, 26);
            this.btn__PortSet.TabIndex = 2;
            this.btn__PortSet.Text = "S E T";
            this.btn__PortSet.UseVisualStyleBackColor = true;
            this.btn__PortSet.Click += new System.EventHandler(this.btn__PortSet_Click);
            // 
            // lb_TimeName
            // 
            this.lb_TimeName.AutoSize = true;
            this.lb_TimeName.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_TimeName.Location = new System.Drawing.Point(264, 14);
            this.lb_TimeName.Name = "lb_TimeName";
            this.lb_TimeName.Size = new System.Drawing.Size(160, 21);
            this.lb_TimeName.TabIndex = 3;
            this.lb_TimeName.Text = "Capture Delay Time";
            // 
            // nud_TimeData
            // 
            this.nud_TimeData.Increment = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.nud_TimeData.Location = new System.Drawing.Point(268, 45);
            this.nud_TimeData.Maximum = new decimal(new int[] {
            5000,
            0,
            0,
            0});
            this.nud_TimeData.Name = "nud_TimeData";
            this.nud_TimeData.Size = new System.Drawing.Size(85, 21);
            this.nud_TimeData.TabIndex = 4;
            // 
            // btn_TimeSet
            // 
            this.btn_TimeSet.Font = new System.Drawing.Font("Nirmala UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_TimeSet.Location = new System.Drawing.Point(368, 41);
            this.btn_TimeSet.Name = "btn_TimeSet";
            this.btn_TimeSet.Size = new System.Drawing.Size(68, 26);
            this.btn_TimeSet.TabIndex = 5;
            this.btn_TimeSet.Text = "S E T";
            this.btn_TimeSet.UseVisualStyleBackColor = true;
            this.btn_TimeSet.Click += new System.EventHandler(this.btn_TimeSet_Click);
            // 
            // btn_FilePath
            // 
            this.btn_FilePath.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_FilePath.Location = new System.Drawing.Point(725, 14);
            this.btn_FilePath.Name = "btn_FilePath";
            this.btn_FilePath.Size = new System.Drawing.Size(120, 55);
            this.btn_FilePath.TabIndex = 6;
            this.btn_FilePath.Text = "File Path";
            this.btn_FilePath.UseVisualStyleBackColor = true;
            this.btn_FilePath.Click += new System.EventHandler(this.btn_FilePath_Click);
            // 
            // pbox_Realtime
            // 
            this.pbox_Realtime.Location = new System.Drawing.Point(32, 94);
            this.pbox_Realtime.Name = "pbox_Realtime";
            this.pbox_Realtime.Size = new System.Drawing.Size(640, 480);
            this.pbox_Realtime.TabIndex = 7;
            this.pbox_Realtime.TabStop = false;
            // 
            // lb_ResultTitle
            // 
            this.lb_ResultTitle.AutoSize = true;
            this.lb_ResultTitle.Font = new System.Drawing.Font("Nirmala UI", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_ResultTitle.Location = new System.Drawing.Point(623, 645);
            this.lb_ResultTitle.Name = "lb_ResultTitle";
            this.lb_ResultTitle.Size = new System.Drawing.Size(106, 32);
            this.lb_ResultTitle.TabIndex = 8;
            this.lb_ResultTitle.Text = "Result : ";
            // 
            // lb_Result
            // 
            this.lb_Result.AutoSize = true;
            this.lb_Result.Font = new System.Drawing.Font("Nirmala UI", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_Result.Location = new System.Drawing.Point(735, 645);
            this.lb_Result.Name = "lb_Result";
            this.lb_Result.Size = new System.Drawing.Size(46, 32);
            this.lb_Result.TabIndex = 9;
            this.lb_Result.Text = "A0";
            // 
            // btn_Start
            // 
            this.btn_Start.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_Start.Location = new System.Drawing.Point(454, 14);
            this.btn_Start.Name = "btn_Start";
            this.btn_Start.Size = new System.Drawing.Size(120, 55);
            this.btn_Start.TabIndex = 10;
            this.btn_Start.Text = "START";
            this.btn_Start.UseVisualStyleBackColor = true;
            this.btn_Start.Click += new System.EventHandler(this.btn_Start_Click);
            // 
            // btn_Stop
            // 
            this.btn_Stop.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_Stop.Location = new System.Drawing.Point(590, 14);
            this.btn_Stop.Name = "btn_Stop";
            this.btn_Stop.Size = new System.Drawing.Size(120, 55);
            this.btn_Stop.TabIndex = 11;
            this.btn_Stop.Text = "STOP";
            this.btn_Stop.UseVisualStyleBackColor = true;
            this.btn_Stop.Click += new System.EventHandler(this.btn_Stop_Click);
            // 
            // pBox_CaptureImg
            // 
            this.pBox_CaptureImg.Location = new System.Drawing.Point(710, 94);
            this.pBox_CaptureImg.Name = "pBox_CaptureImg";
            this.pBox_CaptureImg.Size = new System.Drawing.Size(640, 480);
            this.pBox_CaptureImg.TabIndex = 12;
            this.pBox_CaptureImg.TabStop = false;
            // 
            // backgroundWorker1
            // 
            this.backgroundWorker1.WorkerReportsProgress = true;
            this.backgroundWorker1.WorkerSupportsCancellation = true;
            this.backgroundWorker1.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorker1_DoWork);
            this.backgroundWorker1.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.backgroundWorker1_ProgressChanged);
            // 
            // btn_Capture
            // 
            this.btn_Capture.Font = new System.Drawing.Font("Nirmala UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_Capture.Location = new System.Drawing.Point(869, 14);
            this.btn_Capture.Name = "btn_Capture";
            this.btn_Capture.Size = new System.Drawing.Size(120, 55);
            this.btn_Capture.TabIndex = 13;
            this.btn_Capture.Text = "Capture";
            this.btn_Capture.UseVisualStyleBackColor = true;
            this.btn_Capture.Click += new System.EventHandler(this.btn_Capture_Click);
            // 
            // btn_test
            // 
            this.btn_test.Location = new System.Drawing.Point(113, 658);
            this.btn_test.Name = "btn_test";
            this.btn_test.Size = new System.Drawing.Size(153, 54);
            this.btn_test.TabIndex = 14;
            this.btn_test.Text = "Test";
            this.btn_test.UseVisualStyleBackColor = true;
            this.btn_test.Click += new System.EventHandler(this.btn_test_Click);
            // 
            // pBox_type1
            // 
            this.pBox_type1.Image = global::SortingTest.Properties.Resources.test_img;
            this.pBox_type1.Location = new System.Drawing.Point(1381, 27);
            this.pBox_type1.Name = "pBox_type1";
            this.pBox_type1.Size = new System.Drawing.Size(220, 140);
            this.pBox_type1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type1.TabIndex = 15;
            this.pBox_type1.TabStop = false;
            // 
            // pBox_type2
            // 
            this.pBox_type2.Image = global::SortingTest.Properties.Resources.test_img2;
            this.pBox_type2.Location = new System.Drawing.Point(1627, 27);
            this.pBox_type2.Name = "pBox_type2";
            this.pBox_type2.Size = new System.Drawing.Size(220, 140);
            this.pBox_type2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type2.TabIndex = 16;
            this.pBox_type2.TabStop = false;
            // 
            // pBox_type3
            // 
            this.pBox_type3.Image = global::SortingTest.Properties.Resources.test_img3;
            this.pBox_type3.Location = new System.Drawing.Point(1381, 199);
            this.pBox_type3.Name = "pBox_type3";
            this.pBox_type3.Size = new System.Drawing.Size(220, 140);
            this.pBox_type3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type3.TabIndex = 17;
            this.pBox_type3.TabStop = false;
            // 
            // pBox_type4
            // 
            this.pBox_type4.Image = global::SortingTest.Properties.Resources.test_img4;
            this.pBox_type4.Location = new System.Drawing.Point(1624, 199);
            this.pBox_type4.Name = "pBox_type4";
            this.pBox_type4.Size = new System.Drawing.Size(220, 140);
            this.pBox_type4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type4.TabIndex = 18;
            this.pBox_type4.TabStop = false;
            // 
            // pBox_type5
            // 
            this.pBox_type5.Image = global::SortingTest.Properties.Resources.test_img5;
            this.pBox_type5.Location = new System.Drawing.Point(1381, 370);
            this.pBox_type5.Name = "pBox_type5";
            this.pBox_type5.Size = new System.Drawing.Size(220, 140);
            this.pBox_type5.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type5.TabIndex = 19;
            this.pBox_type5.TabStop = false;
            // 
            // pBox_type6
            // 
            this.pBox_type6.Image = global::SortingTest.Properties.Resources.test_img6;
            this.pBox_type6.Location = new System.Drawing.Point(1624, 370);
            this.pBox_type6.Name = "pBox_type6";
            this.pBox_type6.Size = new System.Drawing.Size(220, 140);
            this.pBox_type6.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type6.TabIndex = 20;
            this.pBox_type6.TabStop = false;
            // 
            // pBox_type7
            // 
            this.pBox_type7.Image = global::SortingTest.Properties.Resources.test_img7;
            this.pBox_type7.Location = new System.Drawing.Point(1381, 541);
            this.pBox_type7.Name = "pBox_type7";
            this.pBox_type7.Size = new System.Drawing.Size(220, 140);
            this.pBox_type7.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type7.TabIndex = 21;
            this.pBox_type7.TabStop = false;
            // 
            // pBox_type8
            // 
            this.pBox_type8.Image = global::SortingTest.Properties.Resources.test_img8;
            this.pBox_type8.Location = new System.Drawing.Point(1627, 541);
            this.pBox_type8.Name = "pBox_type8";
            this.pBox_type8.Size = new System.Drawing.Size(220, 140);
            this.pBox_type8.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pBox_type8.TabIndex = 22;
            this.pBox_type8.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(1466, 684);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(56, 16);
            this.label1.TabIndex = 23;
            this.label1.Text = "Type7";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label2.Location = new System.Drawing.Point(1713, 684);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(56, 16);
            this.label2.TabIndex = 24;
            this.label2.Text = "Type8";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label3.Location = new System.Drawing.Point(1466, 513);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(56, 16);
            this.label3.TabIndex = 25;
            this.label3.Text = "Type5";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label4.Location = new System.Drawing.Point(1713, 513);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(56, 16);
            this.label4.TabIndex = 26;
            this.label4.Text = "Type6";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label5.Location = new System.Drawing.Point(1466, 342);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(56, 16);
            this.label5.TabIndex = 27;
            this.label5.Text = "Type3";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label6.Location = new System.Drawing.Point(1713, 342);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(57, 16);
            this.label6.TabIndex = 28;
            this.label6.Text = "Type4";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label7.Location = new System.Drawing.Point(1466, 170);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(56, 16);
            this.label7.TabIndex = 29;
            this.label7.Text = "Type1";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("굴림", 12F, System.Drawing.FontStyle.Bold);
            this.label8.Location = new System.Drawing.Point(1713, 170);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(56, 16);
            this.label8.TabIndex = 30;
            this.label8.Text = "Type2";
            // 
            // Fm_Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1862, 774);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pBox_type8);
            this.Controls.Add(this.pBox_type7);
            this.Controls.Add(this.pBox_type6);
            this.Controls.Add(this.pBox_type5);
            this.Controls.Add(this.pBox_type4);
            this.Controls.Add(this.pBox_type3);
            this.Controls.Add(this.pBox_type2);
            this.Controls.Add(this.pBox_type1);
            this.Controls.Add(this.btn_test);
            this.Controls.Add(this.btn_Capture);
            this.Controls.Add(this.pBox_CaptureImg);
            this.Controls.Add(this.btn_Stop);
            this.Controls.Add(this.btn_Start);
            this.Controls.Add(this.lb_Result);
            this.Controls.Add(this.lb_ResultTitle);
            this.Controls.Add(this.pbox_Realtime);
            this.Controls.Add(this.btn_FilePath);
            this.Controls.Add(this.btn_TimeSet);
            this.Controls.Add(this.nud_TimeData);
            this.Controls.Add(this.lb_TimeName);
            this.Controls.Add(this.btn__PortSet);
            this.Controls.Add(this.lb_PortName);
            this.Controls.Add(this.cbo_Portnum);
            this.Name = "Fm_Main";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Fm_Main_FormClosing);
            this.Load += new System.EventHandler(this.Fm_Main_Load);
            ((System.ComponentModel.ISupportInitialize)(this.nud_TimeData)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbox_Realtime)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_CaptureImg)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type6)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type7)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pBox_type8)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox cbo_Portnum;
        private System.Windows.Forms.Label lb_PortName;
        private System.Windows.Forms.Button btn__PortSet;
        private System.Windows.Forms.Label lb_TimeName;
        private System.Windows.Forms.NumericUpDown nud_TimeData;
        private System.Windows.Forms.Button btn_TimeSet;
        private System.Windows.Forms.Button btn_FilePath;
        private System.Windows.Forms.Label lb_ResultTitle;
        private System.Windows.Forms.Label lb_Result;
        private System.Windows.Forms.Button btn_Start;
        private System.Windows.Forms.Button btn_Stop;
        public System.Windows.Forms.PictureBox pbox_Realtime;
        public System.Windows.Forms.PictureBox pBox_CaptureImg;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.Button btn_Capture;
        private System.Windows.Forms.Button btn_test;
        private System.Windows.Forms.PictureBox pBox_type1;
        private System.Windows.Forms.PictureBox pBox_type2;
        private System.Windows.Forms.PictureBox pBox_type3;
        private System.Windows.Forms.PictureBox pBox_type4;
        private System.Windows.Forms.PictureBox pBox_type5;
        private System.Windows.Forms.PictureBox pBox_type6;
        private System.Windows.Forms.PictureBox pBox_type7;
        private System.Windows.Forms.PictureBox pBox_type8;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
    }
}

