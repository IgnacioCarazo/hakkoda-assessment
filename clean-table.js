const snowflake = require('snowflake-sdk');
require('dotenv').config(); // Load environment variables from .env file

// Connection parameters
const config = {
  account: process.env.SNOWFLAKE_ACCOUNT,
  username: process.env.SNOWFLAKE_USERNAME,
  password: process.env.SNOWFLAKE_PASSWORD,
  warehouse: process.env.SNOWFLAKE_WAREHOUSE,
  database: process.env.SNOWFLAKE_DATABASE,
  schema: process.env.SNOWFLAKE_SCHEMA,
  role: process.env.SNOWFLAKE_ROLE
};

// Create a connection object
const connection = snowflake.createConnection(config);

// Connect to Snowflake
connection.connect((err, conn) => {
  if (err) {
    console.error('Error connecting to Snowflake:', err);
  } else {
    console.log('Successfully connected to Snowflake');
    // Perform queries or other operations here
    // Example: connection.execute(...)
  }
});

// Close the connection when done
connection.destroy((err) => {
  if (err) {
    console.error('Error closing connection:', err);
  } else {
    console.log('Connection closed');
  }
});