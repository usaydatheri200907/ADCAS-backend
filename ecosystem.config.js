module.exports = {
    apps : [{
      name: 'flask-app',
      script: 'app.py',
      interpreter: 'python',
      watch: true,
      ignore_watch: ['node_modules', 'uploads'],
      env: {
        PORT: 5001,
        FLASK_ENV: 'development',
      },
      env_production: {
        PORT: 5001,
        FLASK_ENV: 'production',
      }
    }]
  };
  