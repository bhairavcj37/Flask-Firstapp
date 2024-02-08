# ..

from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Generate a sample plot
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Convert the BytesIO stream to base64 encoding
    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

    # Close the Matplotlib plot
    plt.close()

    # Pass the base64-encoded image to the template
    return render_template('index.html', image_base64=image_base64)

if __name__ == '__main__':
    app.run(debug=True)

