from flask import Flask, render_template, request, redirect
import youtube_dl



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
  
@app.route('/download', methods=["POST", "GET"])
def download():
	try:
		url = request.form["url"]
		with youtube_dl.YoutubeDL() as ydl:

			url = ydl.extract_info(url, download=False)

			try:
				download_link = url["entries"][-1]["formats"][-1]["url"]
			except:
				download_link = url["formats"][-1]["url"]

			if ".mp4" in download_link:
				return redirect(download_link)
			else:
				return redirect(download_link+"&dl=1")
	except:
		return render_template('index.html')
