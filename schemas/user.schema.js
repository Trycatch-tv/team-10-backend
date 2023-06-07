const Joi = require('joi');

const id = Joi.number().integer();
const userName = Joi.string();
const password = Joi.string();

const createUserSchema = Joi.object({
  userName: userName.required(),
  password: password.required(),
});

const updateUserSchema = Joi.object({
  userName: userName,
});

const getUserSchema = Joi.object({
  id: id.required(),
});

module.exports = { createUserSchema, updateUserSchema, getUserSchema }
