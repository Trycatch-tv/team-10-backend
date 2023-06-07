const express = require("express");
const authenticateMiddleware = require("../middlewares/autentication.handler");

const ItemsService = require("../services/items.service");
const validationHandler = require("../middlewares/validator.handler");
const {
  createItemSchema,
  updateItemSchema,
  deleteItemsSchema,
} = require("../schemas/items.schema");

const router = express.Router();
const service = new ItemsService();

router.get("/", authenticateMiddleware, async (req, res, next) => {
  try {
    res.json(await service.find());
  } catch (error) {
    next(error);
  }
});

router.get("/:name", authenticateMiddleware, async (req, res, next) => {
  try {
    const { name } = req.params;
    res.json(await service.findOne(name));
  } catch (error) {
    next(error);
  }
});

router.post(
  "/",
  authenticateMiddleware,
  validationHandler(createItemSchema, "body"),
  async (req, res, next) => {
    try {
      const body = req.body;
      res.status(201).json(await service.create(body));
    } catch (error) {
      next(error);
    }
  }
);

router.put(
  "/:name",
  authenticateMiddleware,
  validationHandler(updateItemSchema, "body"),
  async (req, res, next) => {
    try {
      const { name } = req.params;
      const body = req.body;
      res.status(201).json(await service.update(name, { ...body, name: name }));
    } catch (error) {
      next(error);
    }
  }
);

router.delete(
  "/:name",
  authenticateMiddleware,
  validationHandler(deleteItemsSchema, "params"),
  async (req, res, next) => {
    try {
      const { name } = req.params;
      await service.delete(name);
      res.status(200).json({ message: "Item deleted" });
    } catch (error) {
      next(error);
    }
  }
);

module.exports = router;
