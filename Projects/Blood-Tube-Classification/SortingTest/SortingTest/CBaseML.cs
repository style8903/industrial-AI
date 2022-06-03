using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Fabric.Management.ServiceModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.ML;
using Microsoft.ML.Data;
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using Microsoft.ML.Transforms.Image;
using Microsoft.ML.Transforms.Onnx;
using OpenCvSharp;

namespace SortingTest
{
    class CBaseML
    {
        static MLContext mLContext = new MLContext();
        static Bitmap ckImage;
        const string model_path = "./models/my_model4.onnx";
        int result_idx;
        static InferenceSession session;

        public void CreateModel()
        {
            session = new InferenceSession(model_path);
            var inputMeta = session.InputMetadata;
        }

        public string PredictResult(Bitmap bitmap)
        {
            /*var emptyData = new List<InputImage>();
            var data = mLContext.Data.LoadFromEnumerable(emptyData);
            var pipline = mLContext.Transforms.ResizeImages(resizing: ImageResizingEstimator.ResizingKind.Fill,
                outputColumnName: "input", imageWidth: 224, imageHeight: 224,
                inputColumnName: nameof(InputImage.Image))
                .Append(mLContext.Transforms.ExtractPixels(outputColumnName: "input"))
                .Append(mLContext.Transforms.ApplyOnnxModel(modelFile: "./models/my_model4.onnx", outputColumnName: "output" , inputColumnName: "input"));


            var model = pipline.Fit(data);

            var predictionEngine = mLContext.Model.CreatePredictionEngine<InputImage, predictResult>(model);
            var labels = File.ReadAllLines("./models/labels.txt");*/

            ckImage = bitmap;
            ckImage = ResizeImage(ckImage, 224, 224);
            result_idx = UseOnnxSession(ckImage, model_path);

            /*var prediction = predictionEngine.Predict(new InputImage { Image = ckImage });*/
            Console.WriteLine($"result : {result_idx + 1}");
            string result = $"Type {result_idx + 1}";
            return result;
        }

        //ONNX 모델 불러오기 및 이미지 Normalize
        public int UseOnnxSession(Bitmap image, string onnxModelPath)
        {
            double[] means = new double[] { 0.485, 0.456, 0.406 };
            double[] stds = new double[] { 0.229, 0.224, 0.225 };
            int max_idx = 0;


            Tensor<float> t1 = ConvertImageToFloatData(image, means, stds);

            var inputs = new List<NamedOnnxValue>()
            {
                NamedOnnxValue.CreateFromTensor<float>("input", t1)
            };
            using (var results = session.Run(inputs))
            {
                foreach (var r in results)
                {
                    var x = r.AsEnumerable<float>().ToArray();

                    float y = x.Max();
                    max_idx = Array.IndexOf(x, y);

                }
            }
            return max_idx;
            
        }

        // Create your Tensor and add transformations as you need.
        public static Tensor<float> ConvertImageToFloatData(Bitmap image, double[] means, double[] std)
        {
            Tensor<float> data = new DenseTensor<float>(new[] { 1, 3, image.Height, image.Width });
            for (int x = 0; x < image.Height; x++)
            {
                for (int y = 0; y < image.Width; y++)
                {
                    Color color = image.GetPixel(x, y);
                    var red = (color.R - (float)means[0] * 255) / ((float)std[0] * 255);
                    var gre = (color.G - (float)means[1] * 255) / ((float)std[1] * 255);
                    var blu = (color.B - (float)means[2] * 255) / ((float)std[2] * 255);
                    data[0, 0, y, x] = red;
                    data[0, 1, y, x] = gre;
                    data[0, 2, y, x] = blu;
                }
            }
            return data;
        }

        public static Bitmap ResizeImage(Image image, int width, int height)
        {
            var destRect = new Rectangle(0, 0, width, height);
            var destImage = new Bitmap(width, height);

            destImage.SetResolution(image.HorizontalResolution, image.VerticalResolution);

            using (var graphics = Graphics.FromImage(destImage))
            {
                graphics.CompositingMode = CompositingMode.SourceCopy;
                graphics.CompositingQuality = CompositingQuality.HighQuality;
                graphics.InterpolationMode = InterpolationMode.HighQualityBicubic;
                graphics.SmoothingMode = SmoothingMode.HighQuality;
                graphics.PixelOffsetMode = PixelOffsetMode.HighQuality;

                using (var wrapMode = new ImageAttributes())
                {
                    wrapMode.SetWrapMode(WrapMode.TileFlipXY);
                    graphics.DrawImage(image, destRect, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel, wrapMode);
                }
            }

            return destImage;
        }
    }

    internal class predictResult
    {
        [VectorType(1,8)]
        [ColumnName("output")]
        public float[] PredictLabels { get; set; }
    }

    internal class InputImage
    {
        [ImageType(224, 224)]

        public Bitmap Image { get; set; }
    }

    
}
