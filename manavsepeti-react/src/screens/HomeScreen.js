import React from "react";
import { Row, Col } from "react-bootstrap";
import ProductCard from "../components/ProductCard";

import products from "../products";

const HomeScreen = () => {
  return (
    <div>
      <h2>Meyve Sebze</h2>
      <Row>
        {products.map((product) => (
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
            <ProductCard product={product} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
