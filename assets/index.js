import { content } from "./content/content.js"
import { Resume } from "./content/resume/resume.js"
import { structure } from "./structure/structure.js"

class Index {
  initialize () {
    structure()
    content()
  }
  resume = new Resume
}

window[ 'index' ] = new Index