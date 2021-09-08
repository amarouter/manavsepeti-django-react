import React from "react";
import { Navbar, Nav, Container, Row } from "react-bootstrap";

const Header = () => {
  return (
    <header>
      <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
        <Container>
          <Navbar.Brand href="/">Manav Sepeti</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="/sepet">
                <i className="fas fa-shopping-cart"></i>Sepetim
              </Nav.Link>
              <Nav.Link href="/giris">
                <i className="fas fa-user"></i>Giriş Yap
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
