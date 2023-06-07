const { Strategy } = require('passport-local');
const boom = require('@hapi/boom');
const bcrypt = require('bcrypt');

const UserService = require('./../../../services/user.service');
const service = new UserService();

const LocalStrategy = new Strategy(
  {
    usernameField: 'userName',
    passwordField: 'password'
  },
  async (userName, password, done) => {
    try {
      const user = await service.findByName(userName);
      if (!user) {
        return done(boom.unauthorized(), false);
      }
      const isMatch = await bcrypt.compare(password, user.password);
      if (!isMatch) {
        return done(boom.unauthorized(), false);
      }
      user.password = undefined;
      return done(null, user);
    } catch (error) {
      return done(error, false);
    }
  }
);

module.exports = LocalStrategy;