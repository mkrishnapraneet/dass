const config = require("config");
const jwt = require("jsonwebtoken");

function auth(req, res, next) {
    const token = req.header("auth-token");

    //check for token
    if (!token) {
        res.status(401).json({ msg: "no token, authorisation denied" });
    }

    try {
        //verify token
        const decoded = jwt.verify(token, config.get("jwtSecret"));
        //add user from payload
        req.user = decoded;
        next();
    }
    catch (e) {
        res.status(400).json({msg: "token is not valid"});
    }

}

module.exports = auth;