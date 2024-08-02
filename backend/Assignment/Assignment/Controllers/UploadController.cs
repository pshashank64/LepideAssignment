using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Assignment.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UploadController : Controller
    {
        // POST api/upload
        [HttpPost]
        public async Task<IActionResult> UploadFile(IFormFile file)
        {
            // Check if the file is null or empty
            if (file == null || file.Length == 0) 
            {
                return BadRequest("No file uploaded!");
            }

            // Create a temporary file to store the uploaded file
            var filePath = Path.GetTempFileName();

            // Copy the uploaded file to the temporary file
            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }

            // Summarize the document using the Python script
            var summary = await SummarizeDocument(filePath);

            // Return the summary as a JSON response
            return Ok(new { summary });
        }

        // Method to summarize the document using the Python script
        private async Task<string> SummarizeDocument(string filePath)
        {
            // Path to the Python script
            var scriptPath = "summarize.py";

            // Configure the process start info for running the Python script
            var processStartInfo = new ProcessStartInfo
            {
                FileName = "python", // Command to execute
                Arguments = $"{scriptPath} {filePath}", // Arguments to pass to the script
                RedirectStandardOutput = true, // Redirect standard output
                RedirectStandardError = true, // Redirect standard error
                UseShellExecute = false, // Do not use shell execute
                CreateNoWindow = true, // Do not create a window
            };

            // Start the process
            using var process = new Process
            {
                StartInfo = processStartInfo
            };

            process.Start();

            // Read the output and error streams
            string result = await process.StandardOutput.ReadToEndAsync();
            string error = await process.StandardError.ReadToEndAsync();

            // Wait for the process to exit
            await process.WaitForExitAsync();

            // Log any errors to the console
            if (!string.IsNullOrEmpty(error))
            {
                System.Console.Error.WriteLine($"Python script error: {error}");
            }

            // Return the result, trimmed of any leading/trailing whitespace
            return result.Trim();
        }
    }
}
