import Header from "../components/Header";

const Control = () => {

    const download = () => {
        const noteContent = document.getElementById('notes').value;
        const filename = document.getElementById('filename').value || 'final_notes';
        const blob = new Blob([noteContent], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = `${filename}.txt`;
        link.click();
    };

    return(

        <div class="main-control">
            <div class="column">
                *Add livestream here* <br />
                {/* Commented out is the livestream url. Replace 10.0.0.46 with robot ip */}
                {/* <img id="camera-stream" src="http://10.0.0.46:8000/stream.mjpg" width="640" height="480" /> */}
            </div>
            <div class="column">
                Notes <br />
                <textarea id="notes" class="notes" rows="15" cols="70" placeholder="Write notes here..." download="final_notes"></textarea>
                <br /><br />
                <button class="saveBtn" onClick={download}> Download</button>
                <input id="filename" class="filename" placeholder="Specify a filename…" />
            </div>
        </div>
    )
};


export default Control;
