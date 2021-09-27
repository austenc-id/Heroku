import { hidden } from "../../style/style.js";
import { aboutme } from "./sections/profile.js";

const aboutmecontent = new aboutme
function transition () {
  document.getElementById( 'title' ).classList.add( hidden )
}

export class Resume {
  profile () {
    transition()
    document.getElementById( 'content' ).classList.remove( hidden )
    document.getElementById( 'content' ).innerHTML = aboutmecontent.text
  }
  work () {
    transition()
  }
  school () {
    transition()
  }
  goals () {
    transition()
  }
  expectations () {
    transition()
  }
}