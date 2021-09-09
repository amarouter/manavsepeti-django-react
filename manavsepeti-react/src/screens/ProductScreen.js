import React from "react";
import { Link } from "react-router-dom";
import {
  Row,
  Col,
  Image,
  ListGroup,
  Button,
  Card,
  ListGroupItem,
} from "react-bootstrap";
import products from "../products";

const ProductScreen = ({ match }) => {
  const product = products.find((p) => p._id === match.params.id);
  return (
    <div>
      <Link to="/" className="btn btn-dark my-3">
        Anasayfa
      </Link>
      <Row>
        <Col md={6}>
          <Image src={product.image} alt={product.name} fluid />
        </Col>

        <Col md={3}>
          <ListGroup variant="flush">
            <ListGroupItem>
              <h4>{product.name}</h4>
            </ListGroupItem>
            <ListGroupItem>Fiyat: {product.price}₺</ListGroupItem>
          </ListGroup>
        </Col>

        <Col md={3}>
          <Card>
            <ListGroup variant="flush">
              <ListGroupItem>
                <Row>
                  <Col>Fiyat:</Col>
                  <Col>
                    <strong>{product.price}₺</strong>
                  </Col>
                </Row>
              </ListGroupItem>

              <ListGroupItem>
                <Row>
                  <Col>Stok:</Col>
                  <Col>
                    {product.countInStock > 0 ? "Mevcut" : "Stokta Yok"}
                  </Col>
                </Row>
              </ListGroupItem>
              <ListGroupItem>
                <Button
                  className="btn-block"
                  disabled={product.countInStock == 0}
                  type="button"
                >
                  Sepete Ekle
                </Button>
              </ListGroupItem>
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default ProductScreen;
