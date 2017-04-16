var debug = process.env.NODE_ENV !== "production";
var webpack = require('webpack');

var financialAccountsUS = './financialAccountsUS/index.jsx'

module.exports = {
  context: __dirname,
  devtool: debug ? "inline-sourcemap" : false,
  entry : {
    // todoApp: todoApp,
    // huiCalculator: huiCalculator,
    // alphaInvestment: alphaInvestment,
    financialAccountsUS: financialAccountsUS,
  },

  // send to distribution
  output: {
    path: __dirname+'/dist/',
    filename: '[name].js'
  },

  module: {
    loaders: [
      {
        test: /.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015','react']
        }
      }
    ]
  },
  plugins: debug ? [] : [
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({ mangle: false, sourcemap: false }),
  ],
};