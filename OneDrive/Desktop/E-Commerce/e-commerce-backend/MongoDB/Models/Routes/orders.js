const express = require('express');
const Order = require('../models/Order');
const router = express.Router();

router.post('/', async (req, res) => {
  const { user, orderItems, totalPrice, paymentStatus } = req.body;
  try {
    const order = await Order.create({ user, orderItems, totalPrice, paymentStatus });
    res.status(201).json({ success: true, data: order });
  } catch (error) {
    res.status(400).json({ success: false, error: error.message });
  }
});

module.exports = router;
