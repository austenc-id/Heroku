import { cap, center, hidden, row } from "../../style/style.js"
import { Templates } from "./templates.js"

const template = new Templates

function title () {
  document.getElementById( 'title' ).setAttribute( 'onclick', 'index.initialize()' )
  document.getElementById( 'title' ).classList.add( row, cap, center )
  document.getElementById( 'title' ).innerHTML = template.title
}
function subtitle () {
  document.getElementById( 'subtitle' ).classList.add( row, cap, center )
  document.getElementById( 'subtitle' ).innerHTML = template.subtitle
}
function details () {
  document.getElementById( 'details' ).classList.add( row, cap, center, hidden )
  document.getElementById( 'details' ).innerHTML = template.details
}

export function header () {
  title()
  subtitle()
  details()
}