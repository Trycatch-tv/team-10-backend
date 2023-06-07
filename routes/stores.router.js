const express = require("express");

const StoreService = require("../services/store.service");
const validationHandler = require("../middlewares/validator.handler");
const {
  createStoreSchema,
  updateStoreSchema,
  getStoreSchema,
  deleteStoreSchema
} = require("../schemas/stores.schema");

const router = express.Router();
const service = new StoreService();

router.get("/", async (req, res, next) => {
  try {
    res.json(await service.find());
  } catch (error) {
    next(error);
  }
});

router.get("/:id"
,validationHandler(getStoreSchema, "params")
, async (req, res, next) => {
  try {
    const { id } = req.params;
    res.json(await service.findOne(id));
  } catch (error) {
    next(error);
  }
});

router.post(
  "/:name",
  validationHandler(createStoreSchema, "params"),
  async (req, res, next) => {
    try {
      const { name } = req.params;
      res.status(201).json(await service.create({name: name}));
    } catch (error) {
      next(error);
    }
  }
);

router.patch(
  "/:id",
  validationHandler(getStoreSchema, "params"),
  validationHandler(updateStoreSchema, "body"),
  async (req, res, next) => {
    try {
      const { id } = req.params;
      const body = req.body;
      res.status(201).json(await service.update(id, body));
    } catch (error) {
      next(error);
    }
  }
);

router.delete(
  "/:name",
  validationHandler(deleteStoreSchema, "params"),
  async (req, res, next) => {
    try {
      const { name } = req.params;
      const result = await service.delete(name);
      res.status(200).json('Store deleted', result);
    } catch (error) {
      next(error);
    }
  }
);

module.exports = router;
