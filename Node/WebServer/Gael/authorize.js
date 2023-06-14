const authorize = (req, res, next) => {
    const {user} = req.query
    if (user === 'Gael'){
        //Setting this request property attaches this data to request indefinitely during the session
        //hence, whole time you navigate app/server, your request object has these data
        req.user = {'name':'Gael', 'id':201989}
        next()
    } else {
        res.status(401).send(`
        <h1> Unauthorized location from User: ${user}. <br><br>
        <a href= '/'> Back to Home </a>
        `)
        next()
    }
  
}

module.exports = authorize;