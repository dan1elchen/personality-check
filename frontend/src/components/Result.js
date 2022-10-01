import React from 'react'

function Result(props) {
    return (
        <div class="Result">
            <div class="Profile">
                {/* <img src="default.jpg"></img> */}
                <p class="username">Daniel Chen</p>
            </div>
            <div class="Output">
                <p>ISTJ</p>
                <p>96% MATCH</p>
                <p>Description</p>
            </div>
        </div>
    )
}

export default Result;