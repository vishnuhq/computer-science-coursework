import './card.styles.css';

const Card = ({ name, email, id }) => {
  return (
    <div className="card-container">
      <img
        alt={`monster ${name}`}
        src={`https://robohash.org/${id}?set=set2&size=180x180`}
      />
      <h3>{name}</h3>
      <p>{email}</p>
    </div>
  );
};

export default Card;
