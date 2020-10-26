const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const PATH_SRC = path.resolve(__dirname, 'src');

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "/dist"),
        filename: "index-bundle.js",
        publicPath: '/'
    },
    module: {
        rules: [
            {
                test: /\.(jpe?g|png|gif|svg|ico)$/i,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: 'images/[name].[ext]',
                        },
                    },
                ],
                exclude: [
                    path.resolve(PATH_SRC, 'fonts'),
                    path.resolve(PATH_SRC, 'images'),
                    /inline/i,
                ],
            },
            {
                test: /\.(jpe?g|png|gif|svg|ico)$/i,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: 'images/[name].[ext]',
                            publicPath: './',
                        },
                    },
                ],
                include: [
                    path.resolve(PATH_SRC, 'images'),
                ],
                exclude: [
                    /inline/i,
                ],
            },
            {
                test: /\.(woff|woff2|eot|otf|ttf|svg)(\?.*$|$)/,
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: 'fonts/[name]-[hash:8].[ext]',
                    },
                }, ],
                include: [
                    path.resolve(__dirname, 'node_modules'),
                    path.resolve(PATH_SRC, 'fonts'),
                ],
                exclude: [
                    /inline/i,
                ],
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                },
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    },
    devServer: {
      historyApiFallback: true,
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        })
    ]
};