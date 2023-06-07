const request = require('supertest');

const createApp = require('../app')

describe('tests for users path', () => {

  let app = null;
  let server = null;
  let api = null;

  beforeEach(() => {
    app = createApp();
    server = app.listen(9000);
    api = request(app);
  });

  describe('POST /auth/login', () => {

    test('should return a 404 Bad request with password invalid', async () => {
      const inputData = {
        userName: "met1",
        password: "-----"
      };
      const { statusCode, body } = await api.post('/api/v1/auth/login/').send(inputData);
      expect(statusCode).toBe(401);
      expect(body.message).toMatch(/Unauthorized/);
    });

    test('should return a 404 Bad request with userName invalid', async () => {
      const inputData = {
        userName: "----",
        password: "najshash1212as"
      };
      const { statusCode, body } = await api.post('/api/v1/auth/login/').send(inputData);
      expect(statusCode).toBe(404);
      expect(body.message).toMatch(/User/);
    });

    test("should return a 200 Bad request with userName valid password valid", async () => {
      const inputData = {
        userName: "met1",
        password: "1234",
      };
      const { statusCode } = await api
        .post("/api/v1/auth/login/")
        .send(inputData);
      expect(statusCode).toBe(200);
    });

  });

  afterEach(() => {
    server.close();
  })
});