import Tweet from "./components/tweet";
class Main extends React.Component {
    render() {
        console.log("Test render")
        return (
            <div>
                <h1>Test microservices Architecture</h1>
            </div>
        );
    }
}
let documentReady = () => {
    console.log("Test DOM")
    ReactDOM.render(
        <Main />,
        document.getElementById('react')
    );
};
$(documentReady);