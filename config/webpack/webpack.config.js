const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

const dev = process.env.NODE_ENV === 'development'

const root = process.cwd()
const src = path.join(root, 'src')
const dist = path.join(root, 'dist')
const context = src

console.log(`ENV: ${process.env.NODE_ENV}`)

const config = {
  context,
  entry: './entry',
  resolve: {
    alias: {
      Components: path.join(src, 'components'),
    },
    extensions: ['.js', '.json', '.jsx'],
  },
  mode: dev ? 'development' : 'production',
  output: {
    path: dist,
    publicPath: '/',
    filename: 'bundle.js',
  },
  module: {
    rules: rules(),
  },
  plugins: plugins(),
  optimization: {
    minimize: !dev,
  },
}

if (dev) {
  console.log('SOURCEMAPPING ON')
  config.devtool = 'eval-source-map'
}

function rules () {
  const localIdentName = !dev ? '[hash:base64:5]' : '[path]___[name]__[local]___[hash:base64:5]'
  return [
    styleRule(localIdentName),
    babel(localIdentName),
  ]
}

function styleRule (localIdentName) {
  return {
    test: /\.s?css$/,
    include: src,
    use: [
      { loader: 'style-loader' },
      {
        loader: 'css-loader',
        options: {
          modules: true,
          sourceMap: true,
          localIdentName,
        },
      },
      { loader: 'sass-loader' },
    ],
  }
}

function babel (localIdentName) {
  return {
    test: /\.jsx?$/,
    include: src,
    use: {
      loader: 'babel-loader',
      options: {
        presets: ['babel-preset-react', 'babel-preset-env'],
        plugins: [
          'babel-plugin-transform-class-properties',
          'babel-plugin-transform-object-rest-spread',
          [
            'react-css-modules',
            {
              context,
              generateScopedName: localIdentName,
            },
          ],
        ],
      },
    },
  }
}


function plugins () {
  return [
    new HtmlWebpackPlugin({
      template: 'index.html',
    }),
  ]
}

module.exports = config
