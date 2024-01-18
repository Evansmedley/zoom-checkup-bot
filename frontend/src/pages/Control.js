import '../assets/Control.css';
import Header from './Header';
const Control = () => {

    return(

        <div class="main-control">
            <Header />
            <div class="column">*Add livestream here*</div>
            <div class="column">
                Notes <br />
                <textarea class="notes" rows="15" cols="70" placeholder="Write notes here..." download="final_notes"></textarea>
                <br /><br />
                <button type='button' class="saveBtn" onclick="download('notes.value', 'filename.value'"> Download</button>
                <input class="filename" placeholder="Specify a filename…" />
            </div>
        </div>
    )
};

function download(text, filename) {
    console.log(5 + 6);
}

export default Control;