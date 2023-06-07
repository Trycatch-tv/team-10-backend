const { Model, DataTypes, Sequelize } = require('sequelize');

const STORES_TABLE = 'stores';

const StoresSchema = {
  id: {
    allowNull: false,
    autoIncrement: true,
    primaryKey: true,
    type: DataTypes.INTEGER
  },
  name: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
  },
  createdAt: {
    allowNull: false,
    type: DataTypes.DATE,
    field: 'created_at',
    defaultValue: Sequelize.fn('now')
  }
};

class Stores extends Model {

  static associate(models) {
    this.hasOne(models.Items, {
      as: "Items",
      foreignKey: "store_id",
    });
  }

  static config(sequelize) {
    return {
      sequelize,
      tableName: STORES_TABLE,
      modelName: 'Stores',
      timestamps: false
    };
  }
}

module.exports = { Stores, StoresSchema, STORES_TABLE };