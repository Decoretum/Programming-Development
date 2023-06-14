const global = (req, res, next) => {
   console.log(`Global Backend function!`);
   next()
}

module.exports = global