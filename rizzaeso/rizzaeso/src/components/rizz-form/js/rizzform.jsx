import React, { useState } from "react";
import "../styles/rizzform.css";

export default function RizzForm() {
  const rizzless = "okaboma";
  const [inputValue, setInputValue] = useState("");
  const [rizz, setRizz] = useState("unknown");

//   Finds rizz chance based on how closely your name relates to okaboma with a bit of luck involved
  function RizzChance(name) {
    name = name.toLowerCase();
    if(name === "okaboma" || name ==="nilai"){
        return 7;
    }
    let count = 0;
    let noRizzCopy = rizzless;
    for (const letter of name) {
      if (noRizzCopy.includes(letter)) {
        if (Math.random() < 0.5) {
            count++;
        }
        noRizzCopy = noRizzCopy.replace(letter, '');
      }
    }
    return count;
  }

  function getRizz(e) {
    e.preventDefault()
    const rizzCount = RizzChance(inputValue);
    setRizz(rizzCount)
  }

  

  return (
    <>
      <h1 className="text-center">Name to Rizz converter</h1>
      <form onSubmit={(e) => getRizz(e)}>
        <div className="mb-3 col-center rizz">
            <label htmlFor="exampleInputEmail1" className="form-label rizzlabel">
            <h3>What's Your Name????</h3>
            </label>
            <input
            type="text"
            className="form-control"
            id="exampleInputEmail1"
            aria-describedby="emailHelp"
            placeholder="Enter name here"
            value={inputValue} // Set input value from state
            onChange={(e) => setInputValue(e.target.value)} // Update state on input change
            />
            <div id="emailHelp" class="form-text">Results may vary as the algorithm is rather complex</div>
            <button
            type="submit"
            className="btn btn-primary mt-3"
            >
            Submit
            </button>
            </div>
        </form>


        <h1 className="text-center">RIZZ: {Number.isInteger(rizz)? Math.round((7-rizz)/7*100): "Unknown"}/100</h1>
    </>
  );
}
