export class Templates {
  get body () {
    return /*html*/`
    <header id="header"></header>
    <nav id="nav"></nav>
    <main id="main"></main>
    <footer id="footer"></footer>
    `
  }
  get header () {
    return /*html*/`
    <h1 id="title"></h1>
    <p id="subtitle"></p>
    `
  }
  get nav () {
    return /*html*/`
      <colm id="nav-1"></colm>
      <colm id="nav-2"></colm>
      <colm id="nav-3"></colm>
      <colm id="nav-4"></colm>
      <colm id="nav-5"></colm>
    `
  }
  get main () {
    return /*html*/`
    <colm id="sb-left"></colm>
    <colm id="content"></colm>
    <colm id="sb-right"></colm>
    `
  }
  get footer () {
    return /*html*/`
    <row id="credits"></row>
    `
  }
}