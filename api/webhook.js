module.exports = (request, response) => {
    response.json({
        body: request.body,
        query: request.query,
        cookies: request.cookies,
    });
};

export default function handler(request, response) {
    response.status(200).json({
        body: request.body,
        query: request.query,
        cookies: request.cookies,
    });
}
