const passport = require('passport');
const jwt = require('jsonwebtoken');
const { config } = require('./../config/config');

// Middleware de autenticación
const authenticateMiddleware = (req, res, next) => {
  passport.authenticate('local', { session: false }, (err) => {
    if (err) {
      return next(err);
    }
    
    // Verificar el token
    const token = req.headers.authorization; // Obtener el token del encabezado de la solicitud
    if (!token) {
      return res.status(401).json({ message: 'Missing token' });
    }
    
    try {
      const decoded = jwt.verify(token, config.jwtSecret);
      req.user = decoded.sub; // Asignar el ID de usuario al objeto de solicitud req.user
      return next();
    } catch (error) {
      return res.status(401).json({ message: 'Invalid token' });
    }
  })(req, res, next);
};

module.exports = authenticateMiddleware;