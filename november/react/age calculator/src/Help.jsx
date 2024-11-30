import "./Help.css";

const Help = () => {
    return (
        <div>
            <h1>Help:</h1>
            <br />
            <h1>How to enter my birth date?</h1>
            <ol>
                <li>At the top of the container, There will be Inputs, You will have to fill them</li>
                <img src="./src/assets/images/example1.png" alt="example1" />
                <br />
                <p className="Completed">And Your are done!</p>
            </ol>
            <br />
            <h1>How to run the ouput?</h1>
            <br />
            <ol>
                <li>Enter your birth day</li>
                <p>Example:</p>
                <img src="./src/assets/images/example1.png" alt="example1" />
                <br />
                <li>At the top of the left corner in the container, There will be a purple button. You must click on it</li>
                <img src="./src/assets/images/example2.png" alt="example2" />
                <p className="Completed">And then Your done!</p>
                <p className="note">Note: Fill the inputs or else it will return an error</p>
            </ol>
            <h1>How to view my age after running the output?</h1>
            <ol>
                <li>Enter your birth day</li>
                <p>Example:</p>
                <img src="./src/assets/images/example1.png" alt="example1" />
                <br />
                <li>At the top of the left corner in the container, There will be a purple button. You must click on it</li>
                <img src="./src/assets/images/example2.png" alt="example2" />
                <p className="note">Note: Fill the inputs or else it will return an error</p>
                <br />
                <li>At the bottom of the container, There will be wroten that how many, Years, Months and days you are</li>
                <p className="Completed">And then Your done!</p>
            </ol>
        </div>
    )
}

export default Help;