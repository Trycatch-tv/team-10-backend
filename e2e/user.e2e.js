const request = require("supertest");

const createApp = require("../app");
const { models } = require('./../libs/sequelize')

describe("tests for users path", () => {
  let app = null;
  let server = null;
  let api = null;

  beforeEach(() => {
    app = createApp();
    server = app.listen(2000);
    api = request(app);
  });

  describe("GET /users", () => {
    test('', async () =>{
        const { statusCode } = await api.get('/api/v1/users/');
        expect(statusCode).toBe(200);
    });
    test('should return a user', async () => {
        const user = await models.User.findByPk('3');
        const { statusCode, body } = await api.get(`/api/v1/users/${user.id}`);
        expect(statusCode).toEqual(200);
        expect(body.id).toEqual(user.id);
      });
  });

  describe("POST /users", () => {
    test("should return a 400 Bad request with user invalid", async () => {
      const inputData = {
        userName: "",
        password: "123456",
      };
      const { statusCode, body } = await api
        .post("/api/v1/users/register/")
        .send(inputData);
      expect(statusCode).toBe(400);
      expect(body.message).toMatch(/userName/);
    });

    test("should return a 400 Bad request with password invalid", async () => {
      const inputData = {
        userName: "metmet",
        password: "",
      };
      const { statusCode, body } = await api
        .post("/api/v1/users/register/")
        .send(inputData);
      expect(statusCode).toBe(400);
      expect(body.message).toMatch(/password/);
    });

    test("should return a 400 Bad request with invalid username password", async () => {
        const inputData = {
          userName: "",
          password: "",
        };
        const { statusCode, body } = await api
          .post("/api/v1/users/register/")
          .send(inputData);
        expect(statusCode).toBe(400);
        expect(body.message).toMatch(/userName/);
        expect(body.message).toMatch(/password/);
      });
  });

  describe("PUT /users", () => {
    test('should return a user valid', async () => {
        const user = await models.User.findByPk('3');
        const inputData = {
            userName: "met",
          };
        const { statusCode } = await api.patch(`/api/v1/users/${user.id}`).send(inputData);
        expect(statusCode).toEqual(200);
      });
  });

  afterEach(() => {
    server.close();
  });
});
