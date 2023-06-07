const boom = require('@hapi/boom');
const bcrypt = require('bcrypt');
const { models } = require('./../libs/sequelize');

class UserService {
  constructor() {}

  async create(data) {
    const hash = await bcrypt.hash(data.password, 10);
    const newUser = await models.User.create({ ...data, password: hash });
    newUser.password = undefined;
    return newUser;
  }

  async find() {
    const rta = await models.User.findAll();
    rta.forEach(user => {
      user.password = undefined;
    });
    return rta;
  }
  
  async findOne(id) {
    const user = await models.User.findByPk(id);
    if (!user) {
      throw boom.notFound('user not found');
    }
    user.password = undefined;
    return user;
  }

  async findByName(userName) {
    const user = await models.User.findOne({ where: { userName } });
    if (!user) {
      throw boom.notFound('User not found');
    }
    return user;
  }
  
  async update(id, changes) {
    const user = await this.findOne(id);
    const rta = await user.update(changes);
    rta.password = undefined;
    return rta;
  }

  async delete(id) {
    const user = await this.findOne(id);
    await user.destroy();
    return { id };
  }
}

module.exports = UserService;
