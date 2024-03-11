from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 
from model.extract_transcript import get_transcript, get_videoid
from model.preprocess import preprocess_transcript

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        video_link = request.form.get('video_link')
        video_id = get_videoid(video_link)
        raw_transcript = get_transcript(video_id)
        transcript = preprocess_transcript(raw_transcript)
        summary = "This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary This is dummy summaryThis is dummy summary "
        response = {
            'transcript': transcript,
            'summary': summary,
            'video_id': video_id
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/download_extension')
def download_extension():
    extension_filename = 'static/extension/chrome_extension.rar'
    return send_file(extension_filename, as_attachment=True)


@app.route('/receive_id', methods=['POST'])
def get_summary():
    try:
        data = request.json
        # video_id = data['video_id']  # Get video_id from JSON data
        # raw_transcript = get_transcript(video_id)
        # transcript = preprocess_transcript(raw_transcript)
        raw_transcript = "hello"
        summary = "The Rocky Mountains, sprawling across the western part of the North American continental shelf, offer a haven for outdoor enthusiasts with activities like hiking, climbing, skiing, and camping. The range's geographical extent is debated, starting north of the Pecos River in New Mexico and extending to the Canadian Provinces of Alberta and British Columbia, with differing definitions between Canada and the US. Three main sections define the Rockies: the Canadian Rockies, Yellowstone National Park, and the elevated region spanning Colorado and Utah, renowned for its numerous peaks over 14,000 feet. Yellowstone, nestled in the heart of the Rockies, showcases its volcanic origin and abundant geothermal features. The Continental Divide of the Americas traverses the Rockies, splitting the continent into Atlantic and Pacific drainage basins, with exceptions like endorheic basins and unique geological features such as Isa Lake and North Two Ocean Creek."
        return jsonify({'transcript': raw_transcript, 'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug="True", host='127.0.0.1', port=5000)
