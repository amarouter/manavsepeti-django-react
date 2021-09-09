import React from "react";
import { Card } from "react-bootstrap";
import { Link } from "react-router-dom";

const ProductCard = ({ product }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <Link to={`/product/${product._id}`}>
        <Card.Img src={product.image} />
      </Link>

      <Card.Body>
        <Link to={`/product/${product._id}`}>
          <Card.Title as="h5">
            <strong>{product.name}</strong>
          </Card.Title>
        </Link>

        <Card.Text as="h5">
          <div className="my-3">{product.price}₺</div>
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default ProductCard;
