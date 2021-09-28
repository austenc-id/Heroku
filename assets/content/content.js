import { col, hidden, sbcol, thumb, ymargin, cap, bold } from "../style/style.js";
import { header } from "./header/header.js";
import { Templates } from "./home/templates.js";
import { navigation } from "./navigation/navigation.js";

const template = new Templates

function leftsidebar () {
  document.getElementById( 'sb-left' ).classList.add( sbcol )
  document.getElementById( 'sb-left' ).innerHTML = template.left
  document.getElementById( 'profile-picture' ).classList.add( thumb, ymargin )
}
function homecontent () {
  document.getElementById( 'content' ).classList.add( col )
  document.getElementById( 'content' ).innerHTML = template.content
  document.getElementById( 'section-title' ).classList.add( cap, ymargin, bold )
}

export function content () {
  document.getElementById( 'sb-right' ).classList.add( sbcol, hidden )
  header()
  navigation()
  leftsidebar()
  homecontent()
}