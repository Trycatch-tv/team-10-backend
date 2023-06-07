const Joi = require("joi");

const id = Joi.number();
const name = Joi.string();

const createStoreSchema = Joi.object({
  name: name.required(),
});

const updateStoreSchema = Joi.object({
  name: name.required(),
});

const getStoreSchema = Joi.object({
  id: id.required(),
});

const deleteStoreSchema = Joi.object({
  name: name.required(),
});

module.exports = {
  createStoreSchema,
  updateStoreSchema,
  getStoreSchema,
  deleteStoreSchema
};