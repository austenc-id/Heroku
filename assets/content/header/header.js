import { cap, center, hide, row } from "../../style/style.js"
import { Templates } from "./templates.js"

const template = new Templates

function title () {
  document.getElementById( 'title' ).classList.add( row, cap, center )
  document.getElementById( 'title' ).innerHTML = template.title
}
function subtitle () {
  document.getElementById( 'subtitle' ).classList.add( row, cap, center )
  document.getElementById( 'subtitle' ).innerHTML = template.subtitle
}
function details () {
  document.getElementById( 'details' ).classList.add( row, cap, center, hide )
  document.getElementById( 'details' ).innerHTML = template.details
}

export function header () {
  title()
  subtitle()
  details()
}