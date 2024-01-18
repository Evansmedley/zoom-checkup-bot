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
                <button type='button' class="saveBtn"> Download</button>
                <input class="filename" placeholder="Specify a filename…" />
            </div>
        </div>
    )
};

export default Control;