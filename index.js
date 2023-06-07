const createApp = require('./app');

const port = 3001;
const app = createApp();

app.listen(port, () => {});
