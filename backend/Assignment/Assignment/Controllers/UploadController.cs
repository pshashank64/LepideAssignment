using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Assignment.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UploadController : Controller
    {
        [HttpPost]
        public async Task<IActionResult> UploadFile(IFormFile file)
        {
            if (file == null || file.Length == 0) 
            {
                return BadRequest("No file uploaded!");
            }

            var filePath = Path.GetTempFileName();

            using(var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }

            var summary = await SummarizeDocument(filePath);

            return Ok(new {summary});

        }

        private async Task<string> SummarizeDocument(string filePath)
        {
            var scriptPath = "summarize.py";

            var processStartInfo = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = $"{scriptPath} {filePath}",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
            };

            using var process = new Process
            {
                StartInfo = processStartInfo
            };

            process.Start();

            string result = await process.StandardOutput.ReadToEndAsync();
            string error = await process.StandardError.ReadToEndAsync();

            await process.WaitForExitAsync();

            if (!string.IsNullOrEmpty(error))
            {
                System.Console.Error.WriteLine($"Python script error: {error}");
            }

            return result.Trim();
        }
    
    }
}
