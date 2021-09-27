import { center, col } from "../../style/style.js";
import { Templates } from "./templates.js";

const template = new Templates

function profile () {
  document.getElementById( 'nav-1' ).setAttribute( 'onclick', 'index.profile()' )
  document.getElementById( 'nav-1' ).classList.add( col, center )
  document.getElementById( 'nav-1' ).innerHTML = template.profile
}
function work () {
  document.getElementById( 'nav-2' ).classList.add( col, center )
  document.getElementById( 'nav-2' ).innerHTML = template.work
}
function school () {
  document.getElementById( 'nav-3' ).classList.add( col, center )
  document.getElementById( 'nav-3' ).innerHTML = template.school
}
function goals () {
  document.getElementById( 'nav-4' ).classList.add( col, center )
  document.getElementById( 'nav-4' ).innerHTML = template.goals
}
function expectations () {
  document.getElementById( 'nav-5' ).classList.add( col, center )
  document.getElementById( 'nav-5' ).innerHTML = template.expectations
}

export function navigation () {
  profile()
  work()
  school()
  goals()
  expectations()
}