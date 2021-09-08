import { Container } from "react-bootstrap";

import Header from "./components/Header";
import Footer from "./components/Footer";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Header />
      <main className="py-3">
        <Container>
          <h1>Hoşgeldiniz</h1>
        </Container>
      </main>
      <Footer />
    </div>
  );
}

export default App;
