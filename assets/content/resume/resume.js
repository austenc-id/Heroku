import { bold, cap, hidden, ymargin } from "../../style/style.js";
import { ambitions } from "./sections/ambitions.js";
import { education } from "./sections/education.js";
import { employment } from "./sections/employment.js";
import { expectations } from "./sections/expectations.js";
import { biography } from "./sections/profile.js";

const bio = new biography
const employ = new employment
const edu = new education
const amb = new ambitions
const expect = new expectations
function transition ( subtitle ) {
  document.getElementById( 'subtitle' ).innerHTML = `<h3>${subtitle}</h3>`
}
function format () {
  document.getElementById( 'section-title' ).classList.add( ymargin, bold )
}

export class Resume {
  profile () {
    transition( 'biography' )
    document.getElementById( 'content' ).innerHTML = bio.text
    format()
  }
  work () {
    transition( 'employment history' )
    document.getElementById( 'content' ).innerHTML = employ.text
    format()
  }
  school () {
    transition( 'formal education' )
    document.getElementById( 'content' ).innerHTML = edu.text
    format()
  }
  goals () {
    transition( 'ambitions' )
    document.getElementById( 'content' ).innerHTML = amb.text
    format()
  }
  expectations () {
    transition( 'expectations' )
    document.getElementById( 'content' ).innerHTML = expect.text
    format()
  }
}