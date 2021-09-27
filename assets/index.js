import { content } from "./content/content.js"
import { structure } from "./structure/structure.js"

class Index {

  initialize () {
    structure()
    content()
  }
}

window[ 'index' ] = new Index