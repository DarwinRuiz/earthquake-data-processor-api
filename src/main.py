from flask import Flask, request, jsonify, send_file
import pandas as pd
import os
import threading

app = Flask(__name__)

def charge_and_clean_earthquakes(csv_file):
    earthquakes_df = pd.read_csv(csv_file)

    # Perform cleanings
    earthquakes_df = earthquakes_df.dropna()        # Delete rows with null values
    earthquakes_df = earthquakes_df.drop_duplicates()  # Remove duplicates

     # Rename columns
    earthquakes_df.rename(columns={
        "FECHA - HORA (UTC)día-mes-año hora:min:seg": "fecha_hora_utc",
        "LATgrados": "lat_grados",
        "LONgrados": "lon_grados",
        "MAGexplicado abajo": "magnitud",
        "PROFkm": "profundidad_km",
        "LOCALIDADhaga clic para ver mapa": "localidad"
    }, inplace=True)

    return earthquakes_df

def delete_file(file_path):
    # Wait a moment to make sure the file has been sent
    WAITING_SECONDS = 10

    threading.Event().wait(WAITING_SECONDS)
    if os.path.exists(file_path):
        os.remove(file_path)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            
            earthquakes_df = charge_and_clean_earthquakes(file)

          
            json_file_path = os.path.join(os.getcwd(), 'sismos_cleaned.json')

            earthquakes_df.to_json(json_file_path, orient='records')

            if not os.path.exists(json_file_path):
                return jsonify({"error": "The JSON file was not created correctly."})
        
            # Start a new thread to delete the file after a few seconds
            threading.Thread(target=delete_file, args=(json_file_path,)).start()

            return send_file(json_file_path, as_attachment=True)

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV file."}), 400

if __name__ == '__main__':
    app.run(debug=True)